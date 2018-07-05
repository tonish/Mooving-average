import TK
import spectral as sp
import numpy

# input file
filename = TK.get_file([('all formats', '.*')], 'select envi file (not .dat file, not hdr file)') #open  radiance image
# #read input
img = sp.envi.open((filename + '.hdr'), filename)
img = img.load()

new_matrix = numpy.zeros_like(img)
weights = numpy.repeat(1.0, 3)/3

for i, j in numpy.ndindex(img.shape[0], img.shape[1]):
    new_matrix[i, j] = numpy.convolve(img[i,j], weights, 'same')

save_name = filename + 'MA3.hdr'
hdr = sp.envi.read_envi_header(filename + '.hdr')
sp.envi.save_image(save_name, new_matrix, metadata=hdr)
print filename
