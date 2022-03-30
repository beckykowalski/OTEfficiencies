//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Script intended to find exposure for analysis thresholds for a dataset.                                                   
// Exposure is added for each channel, determined by the RunsManager Database calculation                                    
// Channels that get included in total exposure have at maximum a desired energy analysis threshold                          
// Analysis threshold determined by algorithm as described in                                                                
// https://docdb.wlab.yale.edu/cuore/RetrieveFile?docid=1959&filename=analysis_energy_thresholds_in_CUORE.pdf&version=1       
//                                                                                                                           
// run with:                                                                                                                 
// root -l                                                                                                                    
// .x $CUORE_INSTALL/lib/diana_root.C                                                                                         
// .L FindExposure.C+                                                                                                        
// FindExposure(<"path_to_datafile">, <"reprocess_string_type">, <int_dataset>, <threshold_level_Desired>, <bool_iscalib>, <bool_print_channels_used>) 
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#include "QGlobalDataManager.hh"
#include "QRunsManagerHandle.hh"
#include "RunsManager.hh"
#include <iostream>
#include <fstream>


void FindExposure(const char* dataPath, const char* reproType, int dataset, double threshLevel, bool isCalib, bool PrintChannels){

  Cuore::QGlobalDataManager dm;
  dm.SetOwner("CuoreMetaData");

  QRunsManagerHandle han("RunsManager");
  han.AddDataset(dataset);
  han.GetOnlyGoodRuns(true);
  han.SetBadAnalysisType(reproType);
  dm.Get(&han, "DB");

  RunsManager runs = han.Get();

  std::map <int, double> ChannelThreshold;

  for(int t=1; t<20; t++){
    ifstream infile;

    if(isCalib){
      infile.open(Form("%s/analysis_energy_thr_from_calibration_ds%d_tower%03d.txt", dataPath, dataset, t));
    }
    else{
      infile.open(Form("%s/analysis_energy_thr_from_background_ds%d_tower%03d.txt", dataPath, dataset, t));
    }
    string temp;
    
    while(std::getline(infile, temp)){
      
      std::stringstream ss(temp);
      string line;
      
      int ch;
      double thr;
      
      int count = 0;
      
      while(ss >> line){
	
	std::stringstream placeholder(line);
	count +=1;
	
	if (count == 1){
	  placeholder >> ch;
	}
	if (count == 2){
	  placeholder >> thr;
	}
      }
      
      ChannelThreshold.insert(pair<int, double>(ch, thr));
      
    }

  }

  std::vector<int> PassingChannels;

  std::map<int, double>::iterator it;
  for(it = ChannelThreshold.begin(); it != ChannelThreshold.end(); it++){
    
    // algorithm to calculate thresholds set's minimum threshold to 5 if the algorithm does not find a true minimum value. Ignore these channels for now. 
    if( (it->second <= threshLevel) && (it->second > 5) ){
      
      PassingChannels.push_back(it->first);

    }

  }

  double exp = 0;
  
  for(int c = 0; c < PassingChannels.size(); c++){
    
    int chan = PassingChannels[c];
    
    if(isCalib){
      exp += runs.GetChannelCalibrationExposure(chan);
    }
    else{
      exp += runs.GetChannelBackgroundExposure(chan);
    }
  }

  if(isCalib){
    std::cout << "Calibration Exposure for channels of under threshold " << threshLevel << " is " << exp << " kg*yr." << std::endl;
  }
  else{
    std::cout << "Background Exposure for channels of under threshold " << threshLevel << " is " << exp << " kg*yr." << std::endl;
  }
  
  if(PrintChannels){
    
    std::cout << "Channels that went into exposure are: ";
    for (int c=0; c< PassingChannels.size(); c++){
      std::cout << PassingChannels[c] << " ";
    }
    std::cout << "" << std::endl;
    
  }

}
