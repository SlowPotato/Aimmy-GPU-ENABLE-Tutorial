# Installing Aimmy with *GPU-ENABLE* Tutorial ==> Nvidia GPU ONLY

1. https://github.com/Babyhamsta/Aimmy/releases/download/v1.3.0/Aimmy1_3_0.zip       ---- EXTRACT to DESKTOP as a single Folder keeping all Contents in the Extracted folder ----

	Download these also: "   https://github.com/Babyhamsta/Aimmy/tree/master/Universalv3_web_model  "      ---- These Master files will be needed later-----

2. https://aka.ms/vs/17/release/vc_redist.x64.exe

3. https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-7.0.14-windows-x64-installer

4. https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

5. https://www.anaconda.com/download  ==> *make your PATH is Enable with Python before completing install*

6. https://developer.nvidia.com/cuda-11-8-0-download-archive    and

   https://developer.nvidia.com/rdp/cudnn-archive    [Download cuDNN v8.9.6 (November 1st, 2023), for CUDA 11.x]

   ![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/2d373454-5fb4-48b3-a7e7-e2c8a3699764)


   Or you can just download the cudNN v8.9.6 files from my Google Drive:   https://drive.google.com/drive/folders/1x6EawdDiXEKicf6b8afnzMBNInx_EpxO?usp=drive_link

Once you have these folders downloaded < bin, lib, include > click on your Windows key, ![adadsdasdasdsdpng](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/cb9b05c2-2d05-4f6e-bc20-258694ca1b90)

Open File Explore and go into you C: and locate *NVIDIA GPU COMPUTING TOOLKIT*

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/c462a682-1e56-49e9-b332-047ef542bc71)

Now going back to the files downloaded from earlier < bin, include and lib >

Open the downloaded: "bin" folder copy all files and paste files directly into the "bin" folder in your C: 
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/ced83e89-d9db-4f36-8715-aeaba6209839)

Do the same for both the "include" and the "lib" folders.

NOTE: The "lib" folder has another folder within itself called "x64" copy the files within that folder, DO NOT COPY AND REPLACE THE EXISTING X64 folder.

Once completed, do the following below:

Type "edit the system environment variables" on windows search and select "environment variables"
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/e11c0e41-9146-4f3b-bc42-0d07b8c1ca32)

see if CUDA PATH and CUDA PATH 11.8 are in the System Variables if they are you should be good to proceed.
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/fefba9a1-35f5-465e-b067-aacc22a9d864)

---Now we can start the Pytorch install---

7. https://pytorch.org/get-started/locally/
	
	  Step1: "Start Locally"
   
	Step2: "Stable 2.1.x"  --> "Windows" --> "Conda" --> "Python" --> "Cuda11.8"

	Step3: "Copy the "Run this Command" "Conda ----------------/cud118"

	Step4. Open "Anoconda Powershell Prompt"

	Step5: Paste the Command and enter

  (This will take Approx 5mins)
  

8. *Anoconda*
Run Command
    - conda install -c conda-forge ultralytics
      
   (This will take Approx 5-10mins)
   
	  - conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
      
    (This will take Approx 5-20mins)

Once that is done we can move onto creating the "Training Folder"

----TRANING FOLDER----

Download the data.yaml file here

 https://www.mediafire.com/file_premium/vv75ynzpromgub4/data.yaml/file

 On your desktop create a Folder and name it, it can be any name will not affect the outcome.
 
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/2b004a27-5994-43d4-ae32-7727ba84bb05)

Paste the data.yaml file inside that Training Folder. 

!!! I renamed my data.yaml file to "CustomCharacterPath" !!! You do not have the change the name of file !!! 

Now create 2 more folders and name them "images" and "labels"

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/1514eb9e-9ada-4d88-8a0e-3b223f2bd2ff)

Within the "images" and "labels" folder create 2 more folders and name them "train" and "val" each.

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/f5566606-71e5-4914-b64f-7a3977788d74)

Now open the data.yaml file as a .txt to edit.

!!This next step is for the "images" folder ONLY!!

Copy the Folder PATH of your "train" folder and paste it in the data.yaml file as such. From RED arrow to GREEN arrow location.

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/88a45c91-797e-467b-bea1-1cbbbf5dbda0)

Do the same for the "val" folder.
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/b735923d-3431-48c1-942e-5b9380c596a0)

Do not exit txt file, click "SAVE" before exiting the data.yaml file

----Gathering Images for Training---

Launch " AimmyWPF " i run this as Admin -- you don't have to though.

Select a "keybind" we will be using this keybind to take screenshots of gameplay

Go to " Settings" - Turn " "ON-Blue" " Collect Data While Playing " - - - will OVERLAY and allow you to snap screenshots everytime "keybind" is pressed,

Launch your Game Client and play a few games *approx 15mins-1 hour of game play * 

The more screenshots you take the better and more efficient the AI will learn *NOTE* Rendering/Training images of large amounts will take hours* THIS IS TO BE EXPECTED

Once you have enough screenshots OPEN your "Aimmy Folder" and " bin " then images      ---- COPY ALL IMAGES over to your Training Folder "IMAGES" ---> "train" and "  val " Folders paste them here.

Now open link browser to create labels for your images.

Now open Link: https://www.makesense.ai/  and Select " Get Started " on bottom right of screen.

Drag and drop all images to the drop box.

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/2132f1a7-fa97-4e4e-a54a-36e733e737d3)

Select "Object Detection"

Insert a label name and put "Enemy"

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/54e17295-f7fc-47a4-a6f0-e0572614428b)


Start Project

On the top left select "Actions" and select "Run AI Locally"

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/d9f69900-cf41-42dd-ba64-5eb95c9c5ac9)

Select YOLOv5 and USE MODEL

Now locate the MODEL MASTER FILES in which was downloaded ealier.

refer back to link: https://github.com/Babyhamsta/Aimmy/tree/master/Universalv3_web_model

Copy all and drag and drop them into the drop bin.
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/6dda430a-4aa4-4565-b8f9-9cda0cc2b94d)

This will make labeling enemy targets on images a bit easier. Place boxes on all targets on all images and once completed.

Go to "Actions" and "Export Annotations"

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/f37b1c5a-10c6-4324-a7b9-b3d9e19b3c0d)

Once downloaded, export/copy/paste all labels into the "Training Folder"--> "labels" ---> "train" and "val"
![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/16047efe-fc1b-4823-b2bc-0cc07de1166a)

Once thats done. We can now start the training of images.

---Training Images---

Copy the PATH of "Training Folder"

Open "Anaconda Powershell Prompt"

type: cd and paste PATH, as such.

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/f9bf6b3d-d2b9-42a6-8b1e-764dfd1d6ff0)

Press ENTER

Now we are in the Directory of the Training Folder paste yolo command: 

yolo task=detect mode=train imgsz=640 data=data.yaml epochs=1000 batch=16 name=             *input a name*

!!NOTE: The higher the epoch the more GPU_Mem you will consume, therefore gameplays will be cut to 30FPS rendering gameplay unplayable so recommend no gampeplays while training.!!

Once that starts you should get GPU_Mem usage as such.

![image](https://github.com/SlowPotato/Aimmy-GPU-ENABLE-Tutorial/assets/152599873/a191f7b3-122c-412f-b6fe-8dd917eedeeb)


----Exporting best.pt to best.ONNX----

Once the Training is completed. Open the "Training Folder" and locate the "runs" ---> "detect" and open the folder with completed results.

Open the "weights" Folder and Copy Folder PATH

Open Anaconda Powershell Prompt

cd and paste folder PATH, ENTER.

Paste Export Yolo command:

yolo export model=best.pt format=onnx

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

best.onnx will be generated in the "Weights Folder" which can now be rename for the game you've made it for. 

Drag and drop onnx file into Aimmy Folder-->bin-->model.


Hope this helps.

Any issue feel free to DM discord:  MentalEngineer#4729









