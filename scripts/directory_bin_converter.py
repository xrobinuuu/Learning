import os


class FileConverter:
    def __init__(self, _input_path):
        self._input_path = _input_path

    def convert_directory_to_bin(self):
        new_dir_path = self._prepare_new_directory(suffix="_converted")
        if not new_dir_path:
            return

        for root, _, files in os.walk(self._input_path):
            target_root = os.path.join(new_dir_path, os.path.relpath(root, self._input_path))
            os.makedirs(target_root, exist_ok=True)
            for file in files:
                self._convert_file_to_bin(os.path.join(root, file), target_root)

    def restore_bin_in_directory(self):
        new_dir_path = self._prepare_new_directory(suffix="_recovered")
        if not new_dir_path:
            return

        for root, _, files in os.walk(self._input_path):
            target_root = os.path.join(new_dir_path, os.path.relpath(root, self._input_path))
            os.makedirs(target_root, exist_ok=True)
            for file in files:
                if file.endswith('.bin'):
                    self._restore_bin_file(os.path.join(root, file), target_root)

    def _prepare_new_directory(self, suffix):
        if not os.path.exists(self._input_path):
            print(f"输入的路径 '{self._input_path}' 不存在。")
            return None
        base_path, dir_name = os.path.split(self._input_path.rstrip(os.sep))
        new_dir_path = os.path.join(base_path, f"{dir_name}{suffix}")
        if os.path.exists(new_dir_path):
            print(f"目标文件夹 '{new_dir_path}' 已存在，请选择其他路径。")
            return None
        os.makedirs(new_dir_path)
        return new_dir_path

    def _convert_file_to_bin(self, source_file_path, target_root):
        target_file_path = os.path.join(target_root, f"{os.path.basename(source_file_path)}.bin")
        try:
            content = self._read_file(source_file_path)
            if content:
                with open(target_file_path, 'wb') as f_tgt:
                    f_tgt.write(content)
        except Exception as e:
            print(f"处理文件 '{source_file_path}' 时出现错误: {e}")

    @staticmethod
    def _restore_bin_file(source_file_path, target_root):
        try:
            with open(source_file_path, 'rb') as f:
                content = f.read()
                target_file_name = os.path.basename(source_file_path).rsplit('.', 1)[0]
                target_file_path = os.path.join(target_root, target_file_name)
                os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
            if content:
                with open(target_file_path, 'wb') as f_tgt:
                    f_tgt.write(content)
        except Exception as e:
            print(f"处理文件 '{source_file_path}' 时出现错误: {e}")

    @staticmethod
    def _read_file(file_path):
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except Exception as e:
            print(f"读取文件 '{file_path}' 时出现错误: {e}")
            return None


def main():
    input_path = input("请输入要转换的文件夹路径: ")
    FileConverter(input_path).convert_directory_to_bin()


if __name__ == "__main__":
    main()
