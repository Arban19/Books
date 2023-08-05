def file_extensions(file_name):
    suffixes = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    file_extensions = file_name.split(".")[-1].lower()
    return suffixes.get(file_extensions, "application/octet-stream")
file_name = input("What is the name of the file: ").lower().strip()
if "." not in file_name:
    file_ext = "application/octet-stream"
else:
    file_ext = file_extensions(file_name)
print(file_ext)
