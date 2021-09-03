# Crater-detection
This repository contains all the tools required to set up and assist the YOLO implementations. There is also a shared Google drive folder that contains essential large files (link: https://drive.google.com/drive/folders/1IoOYq4lGTFjVdtlSFHl5dwrGfO0WclMg?usp=sharing)
The working directory should be set up as follows:

```
/working-directory
    /crater-datasets
    /yolov3
        /data
            lunardata_yolov3_train.yaml
            lunardata_yolov3_test.yaml
            marsdata_yolov3_train.yaml
            marsdata_yolov3_test.yaml
        /model
            yolov3_custom.yaml
        train_tr.py

    /yolov5
        /data
            lunardata_yolov5_train.yaml
            lunardata_yolov5_test.yaml
            marsdata_yolov5_train.yaml
            marsdata_yolov5_test.yaml
        /model
            yolov5m_custom.yaml
    
    count_filter.py
    data_extract.py
    generate_txt.py
    lunar_dataset_create.py
    remove_id.py
    size_filter.py

```

As shown most of the python (.py) modules require to be next to the yolo directories. Hence once the Crater-detection is cloned, it can be treated as the working-directory, or its tools can be moved or copied to the working directory instead.


A detailed description on how to use the modules and files are shown in the main code: 'Crater_Detection_Tutorial.ipynb'. The notebook 'Demo_connect_Robbins_LROC.ipynb' provides a playground demonstration on how the Robbins lunar database is connected to the lunar mosaic (the method is transferable to connecting the Robbins mars database to the Mars THEMIS mosaics). Both Jupyter notebook files are intended to uploaded and run on Google Colabs. 

