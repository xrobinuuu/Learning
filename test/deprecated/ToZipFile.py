import pathlib
import zipfile
import os


# def write_file(dir_path, out_path):
#     files = os.listdir(dir_path)
#     print(files)
#     for file in files:
#         if os.path.isdir(os.path.join(dir_path, file)):
#             new_dir_path = os.path.join(dir_path, file)
#             if not os.path.exists(new_dir_path):
#                 os.mkdir(new_dir_path)
#             write_file(new_dir_path, out_path)
#         else:
#             file_path = os.path.join(dir_path, file)
#             file_out_path = os.path.join(out_path, "file1.zip")
#             print(file_path)
#             with zipfile.ZipFile(file=file_out_path, mode='a', compression=zipfile.ZIP_DEFLATED) as f:
#                 f.write(file_path)
#
#
# if __name__ == "__main__":
#
#     write_file(r"D:\4.Tools\QQPlayer", r"D:\1.Files")


def dir2zip(p, zp):
    for f in p.rglob("*"):
        if f.is_file():
            with zipfile.ZipFile(zp, 'a', zipfile.ZIP_DEFLATED) as z:
                print("---->", f, "---->", p.parent)
                print("****>>", f, str(f.relative_to(p.parent)))
                print(dir(f))
                z.write(f, arcname=str(f.relative_to(p.parent)))


if __name__ == "__main__":
    pth = pathlib.Path(__file__).resolve().parent
    print("pth:", pth)
    zip_pth = pathlib.Path(__file__).resolve().parent.joinpath("rf_v3.zip")
    print("zip_pth:", zip_pth)
    dir2zip(pth, zip_pth)
