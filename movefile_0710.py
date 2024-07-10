# import os
# import shutil

# base_dir = '/Users/shenchingfeng/Library/Containers/com.ootpdevelopments.ootp25macqlm/Data/Application Support/Out of the Park Developments/OOTP Baseball 25/saved_games'
# organized_path = '/Users/shenchingfeng/Downloads/organized_csv'

# # for item in os.listdir(base_dir):
# #     if item.endswith('.lg'):
# #         csv_folder_path = os.path.join(base_dir, item, 'dump', 'dump_2024_03', item[:-3])
# #         if os.path.isdir(csv_folder_path):
# #             destination_path = os.path.join(organized_path, item[:-3])
# #             shutil.move(csv_folder_path, destination_path)
# #         else:
# #             pass

# files = []
# for f in range(160):
#     if f < 10:
#         files.append(f"40320_1600{f}")
#     elif 10 <= f < 100:
#         files.append(f"40320_160{f}")
#     elif 100 <= f < 1000:
#         files.append(f"40320_16{f}")

# for item in os.listdir(organized_path)[:10]:

t = 250
print(t%50)
    