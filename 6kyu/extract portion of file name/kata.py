# class FileNameExtractor:
#     @staticmethod
#     def extract_file_name(dirty_file_name):
#         left, right = 0, dirty_file_name.rfind(".")
#         while dirty_file_name[left].isdigit():
#             left += 1
#         return dirty_file_name[left + 1 : right]


class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        i = dirty_file_name.find("_")
        j = dirty_file_name.rfind(".")
        return dirty_file_name[i + 1 : j]
