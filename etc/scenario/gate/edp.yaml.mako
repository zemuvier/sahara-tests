edp_jobs_flow:
  fake:
    - type: Pig
      input_datasource:
        type: swift
        source: sahara_tests/scenario/defaults/edp-examples/edp-pig/trim-spaces/data/input
      output_datasource:
        type: hdfs
        destination: /user/hadoop/edp-output
      main_lib:
        type: swift
        source: sahara_tests/scenario/defaults/edp-examples/edp-pig/trim-spaces/example.pig
      additional_libs:
        - type: swift
          source: sahara_tests/scenario/defaults/edp-examples/edp-pig/trim-spaces/udf.jar
