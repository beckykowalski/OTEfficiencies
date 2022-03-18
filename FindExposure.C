{

  Cuore::QGlobalDataManager dm;
  dm.SetOwner("CuoreMetaData");

  QRunsManagerHandle han("RunsManager");
  han.AddDataset(3519);
  han.GetOnlyGoodRuns(true);
  han.SetBadAnalysisType("ReproSpring19");
  dm.Get(&han, "DB");

  vector<int> thresh;
  thresh.push_back(10);
  thresh.push_back(15);

  for(int thr = 0 ; thr<thresh.size(); thr++){

    ifstream infile;
    infile.open(Form("ds3519_analysis_thresholds/ds3519_%d.txt", thresh[thr]));
    
    RunsManager runs = han.Get();
    
    float exp = 0;

    string tp;
    while(getline(infile, tp)){
      
      
      stringstream s;
      int chan;

      s << tp;
      s >> chan;
      
      //      std::cout << runs.GetChannelBackgroundExposure(chan) << std::endl;

      //      exp += runs.GetChannelBackgroundExposure(chan);
      exp += runs.GetChannelCalibrationExposure(chan);

    }

    std::cout << "Exposure of channels with analysis thresholds < " << thresh[thr] << " keV is " << exp << " kg.yr." << std::endl; 

  }


}
