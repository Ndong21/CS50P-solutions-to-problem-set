suffixes: list[str] = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

filename: str = input("File name: ")


file_format: str = filename.rsplit(".", maxsplit=1)[-1]
print(file_format)

match file_format:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "zip":
        print("application/zip")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "gif":
        print("image/gif")
    case _:
        print("application/octet-stream")
