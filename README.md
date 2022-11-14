SumEval
Helper Code and Datasets for the 1st Workshop on Scaling Up Multilingual Evaluation (SUMEval).

Test sets containing new configurations but same languages as seen in the training data. These are often denoted without any suffix, for eg: data/test_release/XNLI_XLMR.json
Test sets containing new languages aka surprise languages but same configurations as the ones seen during training. These are denoted by the suffix '_surprise_langs_same_configs', for eg: data/test_release/XNLI_XLMR_surprise_langs_same_configs.json
Test sets containing surprise languages as well as new configurations. These are denoted by the suffix '_surprise_langs_diff_configs', for eg: data/test_release/XNLI_XLMR_surprise_langs_diff_configs.json
All the test files are of the following format:

[
  {
    "train_config": {
      "<train_lang_1>": "<Size(train_lang_1)>",
      .,
      .,
      .,
      "<train_lang_n>": "<Size(train_lang_n)>",
    },
    "eval_results" : {
      "<eval_lang_1>" : "x",
      .,
      .,
      .,
      "<eval_lang_m>" : "x",
    }
  
  }

]
The participants predict the "x" values in these files by training predictor models on the training data, and replace "x" with the predicted values in these files. For instance one can generate the predictions using the LITMUS predictor baseline by running:

python -m src.sum_eval_predict --data_dir ./data --out_dir ./Baselines --model xlmr
python -m src.sum_eval_predict --data_dir ./data --out_dir ./Baselines --model tulrv6

This will generate predictions for each file in the ./Baselines/preds directory.

To run the GMU-Task+Model system, one can generate predictions using the following command:

python -m src.sum_eval_predict --data_dir ./data --out_dir ./Baselines --model both

To create the ensemble predictions, run the following:

python ensemble.py --output_data_path1 $Input_Prediction_directory1 --output_data_path2 $Input_Prediction_directory2 --output_ensemble_data_dir $OUTPUT_Directory

