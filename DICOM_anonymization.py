# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:05:56 2021

@author: MOUMOU
"""

import pydicom
import os
import numpy as np

path = r"TSA"
studies = np.array([[(os.path.join(dp, f), pydicom.dcmread(os.path.join(dp, f), stop_before_pixels = False)) for f in files] for dp,_,files in os.walk(path) if len(files) != 0])

#---------------------------------------Some visualization-----------------------------------------#
dcm_file = studies[0][0][1]
print(dcm_file)

# Save a dcm preview
file = open("dcm_sample.txt", "w")
file.write("%s = %s\n" %("dcm_sample : ", dcm_file))

file.close()

print(dcm_file.PatientName)
print(dcm_file.PatientID)
print(dcm_file.IssuerOfPatientID)
print(dcm_file.PatientBirthDate)
print(dcm_file.PatientSex)
print(dcm_file.PatientAge)
print(dcm_file.PatientWeight)
print(dcm_file.PatientState)
print(dcm_file.SpecialNeeds)
print(dcm_file.MedicalAlerts)
print(dcm_file.Allergies)
print(dcm_file.EthnicGroup)
print(dcm_file.Occupation)
print(dcm_file.AdditionalPatientHistory)
print(dcm_file.PregnancyStatus)
print(dcm_file.PatientComments)

print(dcm_file.StudyDate)
print(dcm_file.StudyID)
print(dcm_file.SeriesDate)
print(dcm_file.ContentDate)
print(dcm_file.StudyTime)
print(dcm_file.SeriesTime)
print(dcm_file.StudyComments)
print(dcm_file.StudyDescription)
print(dcm_file.SeriesDescription)
print(dcm_file.AcquisitionDate)
print(dcm_file.AcquisitionTime)
print(dcm_file.ContentTime)
print(dcm_file.AccessionNumber)
print(dcm_file.InstanceCreationDate)
print(dcm_file.InstanceCreationTime)

print(dcm_file.InstitutionName)
print(dcm_file.InstitutionAddress)
print(dcm_file.InstitutionalDepartmentName)
print(dcm_file.PerformingPhysicianName)
print(dcm_file.ScheduledPerformingPhysicianName)
print(dcm_file.ReferringPhysicianName)
print(dcm_file.OperatorsName)
print(dcm_file.StationName)
print(dcm_file.DeviceSerialNumber)
print(dcm_file.PerformedProcedureStepStartDate)
print(dcm_file.PerformedProcedureStepStartTime)
print(dcm_file.PerformedProcedureStepEndDate)
print(dcm_file.PerformedProcedureStepEndTime)
print(dcm_file.PerformedProcedureStepStatus)
print(dcm_file.PerformedProcedureStepID)
print(dcm_file.PerformedProcedureStepDescription)
print(dcm_file.PerformedProcedureTypeDescription)
print(dcm_file.RequestingService)
print(dcm_file.PerformedStationName)
print(dcm_file.PerformedLocation)

#----------De-identification per the Basic Confidentiality Profile, with "Retain UIDs" option--------------#
# To understand the anonymization technique, please check the table in : http://dicom.nema.org/medical/dicom/2020a/output/chtml/part15/chapter_E.html

def AnonymizeDICOMDataset(ds):
    
#-----------Patient info------------#    
    
    ds.PatientName = "Anonymous"
    ds.PatientID = ""
    if ("IssuerOfPatientID" in ds):
        del ds.IssuerOfPatientID
    ds.PatientBirthDate = "19500101" #Replace it by dummy value
    ds.PatientSex = ""
    if ("PatientAge" in ds):
        del ds.PatientAge
    if ("PatientWeight" in ds):
        del ds.PatientWeight
    if ("PatientState" in ds):
        del ds.PatientState
    if ("SpecialNeeds" in ds):
        del ds.SpecialNeeds
    if ("MedicalAlerts" in ds):
        del ds.MedicalAlerts
    if ("Allergies" in ds):
        del ds.Allergies    
    if ("EthnicGroup" in ds):
        del ds.EthnicGroup     
    if ("Occupation" in ds):
        del ds.Occupation
    if ("AdditionalPatientHistory" in ds):
        del ds.AdditionalPatientHistory
    if ("PregnancyStatus" in ds):
        del ds.PregnancyStatus
    if ("PatientComments" in ds):
        del ds.PatientComments

#----------Acquisition info-----------------#
  
    ds.StudyDate = "19900101" #Replace it by dummy value
    ds.StudyID = ""
    ds.SeriesDate = "19900101" #Replace it by dummy value
    ds.ContentDate = ""
    ds.StudyTime = ""
    if ("SeriesTime" in ds):
        del ds.SeriesTime
    if ("StudyComments" in ds):
        del ds.StudyComments    
    if ("StudyDescription" in ds):
        del ds.StudyDescription    
    if ("SeriesDescription" in ds):
        del ds.SeriesDescription    
    if ("AcquisitionDate" in ds):
        del ds.AcquisitionDate    
    if ("AcquisitionTime" in ds):
        del ds.AcquisitionTime    
    if ("ContentTime" in ds):
        del ds.ContentTime    
    ds.AccessionNumber = ""      
    if ("InstanceCreationDate" in ds):
        del ds.InstanceCreationDate
    if ("InstanceCreationTime" in ds):
        del ds.InstanceCreationTime

#-------------Hospital info--------------#
 
    if ("InstitutionName" in ds):
        del ds.InstitutionName
    if ("InstitutionAddress" in ds):
        del ds.InstitutionAddress
    if ("InstitutionalDepartmentName" in ds):
        del ds.InstitutionalDepartmentName
    if ("PerformingPhysicianName" in ds):
        del ds.PerformingPhysicianName
    if ("ScheduledPerformingPhysicianName" in ds):
        del ds.ScheduledPerformingPhysicianName
    ds.ReferringPhysicianName = ""  
    if ("OperatorsName" in ds):
        del ds.OperatorsName
    if ("StationName" in ds):
        del ds.StationName
    if ("DeviceSerialNumber" in ds):
        del ds.DeviceSerialNumber
    if ("PerformedProcedureStepStartDate" in ds):
        del ds.PerformedProcedureStepStartDate   
    if ("PerformedProcedureStepStartTime" in ds):
        del ds.PerformedProcedureStepStartTime
    if ("PerformedProcedureStepEndDate" in ds):
        del ds.PerformedProcedureStepEndDate
    if ("PerformedProcedureStepEndTime" in ds):
        del ds.PerformedProcedureStepEndTime  
    if ("PerformedProcedureStepStatus" in ds):
        del ds.PerformedProcedureStepStatus  
    if ("PerformedProcedureStepID" in ds):
        del ds.PerformedProcedureStepID
    if ("PerformedProcedureStepDescription" in ds):
        del ds.PerformedProcedureStepDescription
    if ("PerformedProcedureTypeDescription" in ds):
        del ds.PerformedProcedureTypeDescription
    if ("RequestingService" in ds):
        del ds.RequestingService
    if ("PerformedStationName" in ds):
        del ds.PerformedStationName
    if ("PerformedLocation" in ds):
        del ds.PerformedLocation
        
    return ds

# to clean up all Private Attributes per the Basic Confidentiality Profile
def StripPrivateTags(ds):
    for t in enumerate(ds):
        if (t[1].tag.is_private):
            del ds[t[1].tag]

#------------------------------------------------Saving anonymized data-----------------------------------------#

def FillAnonymizationMeta(ds):
    # Meta information
    
    # Preamble needs to be 128 bytes long
    preamble_str = b"Data Anonymizer"
    preamble = bytearray(preamble_str)
    preamble.extend([0 for _ in range(0,128-len(preamble_str))])

    ds.preamble = preamble
    
    ds.file_meta.ImplementationVersionName = "VERSION_1"
    ds.file_meta.SourceApplicationEntityTitle = "Anonymization TSA Rothschild"
    
    # De-id stuff

    ds.PatientIdentityRemoved = "YES"
    ds.DeidentificationMethod = "De-identification data" 
    
    ds.DeidentificationMethodCodeSequence = [pydicom.Dataset()]
    ds.DeidentificationMethodCodeSequence[0].CodingSchemeDesignator = "DCM"
    ds.DeidentificationMethodCodeSequence[0].CodeMeaning = "Basic Application Confidentiality Profile"
    ds.DeidentificationMethodCodeSequence[0].CodeValue = "113100"

    ds.DeidentificationMethodCodeSequence += [pydicom.Dataset()]
    ds.DeidentificationMethodCodeSequence[1].CodingSchemeDesignator = "DCM"
    ds.DeidentificationMethodCodeSequence[1].CodeMeaning = "Retain UIDs Option"
    ds.DeidentificationMethodCodeSequence[1].CodeValue = "113110"


# Do this for all images in series and save them:
for std in studies:
    series = std 
    for s in series:
        print(s[0])
        AnonymizeDICOMDataset(s[1])
        StripPrivateTags(s[1])
        FillAnonymizationMeta(s[1])
        split = s[0].split("\\")
        dst_path = 'TSA_data_anonymized_dst\\' + split[1] + "\\" + split[2]
        s[1].save_as(dst_path)

# Verify if data is de-id
path_deidentification = r"TSA_data_anonymized_dst"
studies_anonymized = np.array([[(os.path.join(dp, f), pydicom.dcmread(os.path.join(dp, f), stop_before_pixels = True)) for f in files] for dp,_,files in os.walk(path_deidentification) if len(files) != 0])

print(studies_anonymized[0][0][1])
print("blabla")
prin("hell")