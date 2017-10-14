import dicom
import os.path
import glob
import sys
import SimpleITK as sitk

def addStudyDateTime(studyPath):
    for file in glob.glob(os.path.join(studyPath, '*.dcm')):
        ds = dicom.read_file(file)
        ds.StudyDate = '20170803'
        ds.StudyTime = '080429.171808'
        ds.save_as(file)
        print('Saved {}'.format(file))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No path specified.')
        sys.exit()
    addStudyDateTime(sys.argv[1])
