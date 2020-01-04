# # import operating system and glob libraries

import os
import glob



# import pydicom library
import pydicom


# grab the name of every file in a folder that must be created called 'files_to_antianonymize' folder
for filename in glob.iglob('files_to_antianonymize/*', recursive=True):
    # read in a DICOM file into memory
    ds = pydicom.read_file(filename, force=True)
    
    # get the name of the folder the dicomfiles are stored in
    foldername = os.path.basename(os.path.dirname(os.path.dirname(filename)))
    
    #get patient name, accesion number, patient ID and patient birthdate
    PatientName = ds.PatientName
    AccessionNumber = ds.AccessionNumber
    PatientID = ds.PatientID
    PatientBirthDate = ds.PatientBirthDate

  
    #put anon on real patient name but fake patient name in ethnic group, accesion number and other info into other tags
    # note ethnic group is a throaway field in the algorithm, but this just shows how this can work
    ds.PatientName = 'Anon'
    ds.EthnicGroup ='Candace'
    #now change the stuff that matters
    ds.ImageType = 'Candace'
   
    # overwrite the original file
    pydicom.write_file(filename,ds)
    
    # output progress to the screen
    print(filename)
    
