import shutil
import os


def move_data(source_folder, destination_folder, data_paths):
    for data_path in data_paths:
        source_image_path = os.path.join(source_folder, 'images', data_path + '.jpg')
        destination_image_path = os.path.join(destination_folder, 'images', data_path)
        
        source_label_path = os.path.join(source_folder, 'labels', data_path + '.txt')
        destination_label_path = os.path.join(destination_folder, 'labels', data_path)
        
        try:    
            shutil.move(source_image_path, destination_image_path)
            shutil.move(source_label_path, destination_label_path)
            print(f"Moved image: {source_image_path} to {destination_folder}/images")
            print(f"Moved label: {source_label_path} to {destination_folder}/labels")
        except FileNotFoundError:
            print(f"File not found: {source_image_path} or {source_label_path}")


# Replace 'path/to' with the actual paths to your folders
train_folder = '/home/khaled/workspace/mx-project/train'
test_folder = '/home/khaled/workspace/mx-project/test'
valid_folder = '/home/khaled/workspace/mx-project/valid'

# List of image paths for Test
test_image_paths = [
    "20231030_073112_jpg.rf.889b4bf54054a064d71ec4b7894c24aa",
    "20231030_073955_jpg.rf.9f5663e2dfac0a391a9bb77d3f5f67db",
    "20231030_074911_jpg.rf.b71bfb1baea89ea622709fd5d30f6524",
    "20231030_080054_jpg.rf.30032e644634b909c5d2c5675723ba1b",
    "20231030_081111_jpg.rf.3b519d4cc768e790c1410367d09bcab1",
    "20231030_081746_jpg.rf.5ab402e27192e184510ca9fa68bf6c8b",
    "20231030_082654_jpg.rf.187b0b85bb05ab215a7147e29d0f3765",
    "20231030_083507_jpg.rf.f6d0fb7eb053e3d31b98a71d4cd83c1d",
    "20231030_084056_jpg.rf.0ae79f751fec2254332457b20dc633f3",
    "20231030_084746_jpg.rf.1cfda7577e27a51772574026fe593b8d",
    "20231030_085403_jpg.rf.bba35d2ca9c81e37d3235533ecf25467",
    "20231030_090538_jpg.rf.81792f318a9ddf856302a17d79fc4db8",
    "20231030_090844_jpg.rf.cd28216da01eacc337cd50e193701724",
    "20231030_090807_jpg.rf.31c32f52feefa82033f263dc91af4036",
    "20231030_090907_jpg.rf.5aeb244845a95fb3323775760d9ba537",
]

# List of image paths for Valid
valid_image_paths = [
    "20231030_073326_jpg.rf.9697633720d578921054ce710047c66e",
    "20231030_073326_jpg.rf.9697633720d578921054ce710047c66e",
    "20231030_074314_jpg.rf.51862d985433ee9cd02bea6ed8439ce1",
    "20231030_075325_jpg.rf.e5883b2123c2837e2db8742e96f417b9",
    "20231030_080811_jpg.rf.b81c2e23e31f8dfe5fa048f9559959bf",
    "20231030_081341_jpg.rf.5a6c3d032b049d4a6bdbfa2b7d7bd84e",
    "20231030_081706_jpg.rf.9d37189ebb3521805b54137ee1d0ccc9",
    "20231030_082214_jpg.rf.ae87a09d3a05fba65e4f96da1aeb5bd2",
    "20231030_082953_jpg.rf.6418c307ceacb78d51f8a8b0dcbaea23",
    "20231030_083659_jpg.rf.69fa18cf228f3ed2a9fa19bd7da9aab3",
    "20231030_084501_jpg.rf.b868925a51cf1e5a59b6ba1124786ea3",
    "20231030_085101_jpg.rf.b51add98203e7ea3f43cf012bc1ae820",
    "20231030_085458_jpg.rf.8c525605db5ebd46ed8f26a31f892996",
    "20231030_090748_jpg.rf.1e2ae43358b6122f5fd3a15d3d736de9",
    "20231030_075258_jpg.rf.dd39d14b0c746156168e951b5532c7a6",
]

# # Move images to Test
# move_data(train_folder, test_folder, test_image_paths)

# # Move images to Valid
# move_data(train_folder, valid_folder, valid_image_paths)

print(len(os.listdir(os.path.join(valid_folder, 'images'))))

