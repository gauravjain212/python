import tarfile

filename = input("Enter the file name to untar: ")

tar_file = tarfile.open(filename,"r")

tar_file.extractall()


print("Extraced Completed")
