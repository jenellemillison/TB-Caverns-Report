import os
import numpy as np
data_path = os.getcwd()
example_filename = os.path.join(data_path, 'TRN_00.nii.gz')
import nibabel as nib
img = nib.load(example_filename)
img.shape
img.get_data_dtype() == np.dtype(np.int16)
img.affine.shape
data = img.get_fdata()
data.shape
type(data)
hdr = img.header
hdr.get_xyzt_units()
raw = hdr.structarr
raw['xyzt_units']
import numpy as np
data = np.ones((32, 32, 15, 100), dtype=np.int16)
img = nib.Nifti1Image(data, np.eye(4))
img.get_data_dtype() == np.dtype(np.int16)
img.header.get_xyzt_units()
nib.save(img, os.path.join('build', 'TRN_00.nii.gz'))