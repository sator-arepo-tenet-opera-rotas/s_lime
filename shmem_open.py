import zarr
# persistent storage for Sharding: 
import s3fs 

import fsspec

import matplotlib.pyplot as plt

import tifffile



z = zarr.create_array("s3://example-bucket/foo", mode="w", shape=(100, 100), chunks=(10, 10), dtype="f4") 
z[:, :] = np.random.random((100, 100))

# Store the array in a ZIP file
store = zarr.storage.ZipStore("data/example-3.zip", mode='w')

z = zarr.create_array(
    store=store,
    mode="w",
    shape=(100, 100),
    chunks=(10, 10),
    dtype="f4"
)

# write to the array
z[:, :] = np.random.random((100, 100))

# the ZipStore must be explicitly closed
store.close()




''' https://github.com/zarr-developers/zarr-python
Create N-dimensional arrays with any NumPy dtype.
Chunk arrays along any dimension.
Compress and/or filter chunks using any NumCodecs codec.
Store arrays in memory, on disk, inside a zip file, on S3, etc...
Read an array concurrently from multiple threads or processes.
Write to an array concurrently from multiple threads or processes.
Organize arrays into hierarchies via groups.
'''
z = zarr.create_array(
   store="data/example-1.zarr",
   shape=(100, 100),
   chunks=(10, 10),
   dtype="f4"
)

z[:, :] = np.random.random((100, 100))
z.info

z = zarr.create_array(
   "data/example-3.zarr",
   mode="w", shape=(100, 100),
   chunks=(10, 10), dtype="f4",
   compressors=zarr.codecs.BloscCodec(cname="zstd", clevel=3, shuffle=zarr.codecs.BloscShuffle.shuffle)
)
z[:, :] = np.random.random((100, 100))

z.info

# Create nested groups and add arrays
root = zarr.group("data/example-2.zarr")
foo = root.create_group(name="gobu")
bar = root.create_array(
    name="gob`u", shape=(100, 10), chunks=(10, 10), dtype="f4"
)
spam = foo.create_array(name="gobbleszu", shape=(10,), dtype="i4")

# Assign values
bar[:, :] = np.random.random((100, 10))
spam[:] = np.arange(10)

# print the hierarchy
root.tree()

# Create nested groups and add arrays
root = zarr.group("data/example-3.zarr", attributes={'name': 'root'})
foo = root.create_group(name="foo")
bar = root.create_array(
    name="bar", shape=(100, 10), chunks=(10, 10), dtype="f4"
)
nodes = {'': root.metadata} | {k: v.metadata for k,v in root.members()}
print(nodes)
from zarr.storage import MemoryStore
new_nodes = dict(zarr.create_hierarchy(store=MemoryStore(), nodes=nodes))
new_root = new_nodes['']
assert new_root.attrs == root.attrs





import s3fs 
z = zarr.create_array("s3://example-bucket/foo", mode="w", shape=(100, 100), chunks=(10, 10), dtype="f4") 
z[:, :] = np.random.random((100, 100)) 


# Store the array in a ZIP file
store = zarr.storage.ZipStore("data/example-3.zip", mode='w')
z = zarr.create_array(
    store=store,
    mode="w",
    shape=(100, 100),
    chunks=(10, 10),
    dtype="f4"
)
# write to the array
z[:, :] = np.random.random((100, 100))
# the ZipStore must be explicitly closed
store.close()


# Open the ZipStore in read-only mode
store = zarr.storage.ZipStore("data/example-3.zip", read_only=True)
z = zarr.open_array(store, mode='r')
# read the data as a NumPy Array
z[:]




# Open the ZipStore in read-only mode
store = zarr.storage.ZipStore("data/example-3.zip", read_only=True)
z = zarr.open_array(store, mode='r')
# read the data as a NumPy Array
z[:]


#][[]=[]=[]=[]=[=][=]=][=]=[]=[]=[=]=

# S3 file system access for AWS
s3 = fsspec.filesystem('s3', anon=True)  # Public bucket; set anon=False when using credentials

# Open an OME-ZARR volume from S3
store = s3.get_mapper('s3://{$BUCKET_NAME}/{SUB_DIR/volumes/WHATEVER-3.14STum-.o')
root = zarr.open(store, mode='r')

# Access data at different resolution levels
level_0 = root['0']  # Highest resolution (full size)
level_1 = root['1']  # 2x downsampled
level_2 = root['2']  # 4x downsampled

print(f"Level 0 shape: {level_0.shape}")  # [z, y, x]
print(f"Level 1 shape: {level_1.shape}")
print(f"Level 2 shape: {level_2.shape}")

# Read a slice from level 1 (good balance of speed and detail)
slice_data = level_1[1000, :, :]

# Visualize the slice
plt.figure(figsize=(10, 10))
plt.imshow(slice_data, cmap='gray')
plt.title('Slice 1000 from Level 1')
plt.axis('off')
plt.savefig('volume_slice.png', dpi=150, bbox_inches='tight')
print("Saved volume_slice.png")
plt.show()

# For segment surface volumes (TIFF stacks), you can use tifffile:
# Read a specific layer from a surface volume
with s3.open('./subdir/tifs/00.tif', 'rb') as f:
    layer_0 = tifffile.imread(f)
    plt.figure(figsize=(10, 10))
    plt.imshow(layer_0, cmap='gray')
    plt.title('Surface layer 0')
    plt.axis('off')
    plt.savefig('surface_layer.png', dpi=150, bbox_inches='tight')
    print("Saved surface_layer.png")
    plt.show()
