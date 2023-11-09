# This function is used for quering doi with the api of Unpaywall
# Importation
import requests

# Defination
# 根据doi尝试访问unpaywall并返回结果
def search(doi):
    url = f"https://api.unpaywall.org/v2/{doi}?email=@.com"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        print("文献在Unpaywall查找成功")
        return json_data
    else:
        print("文献在Unpaywall查找失败，状态码:", response.status_code,"，请检查提供的doi是否正确！")
        return None

# Test Code
if __name__ == "__main__":
    print("输入DOI，以在Unpaywall查询；",end="")
    doi = input()
    json = search(doi)
    if json:
        print("取得的json可被用于下游代码")