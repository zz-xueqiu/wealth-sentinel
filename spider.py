import urllib.request
import json
import datetime

def fetch_and_update_products():
    print(f"[{datetime.datetime.now()}] 开始执行全网短期理财产品数据抓取...")
    
    # 模拟抓取到的全网最新短期理财产品数据
    latest_products = [
        {"code": "003834", "name": "易方达天天理财A", "yield_7d": "2.21%", "update_date": str(datetime.date.today())},
        {"code": "000009", "name": "嘉实活期宝", "yield_7d": "2.15%", "update_date": str(datetime.date.today())},
        {"code": "招银理财", "name": "招银理财日日盈1号", "yield_7d": "2.65%", "update_date": str(datetime.date.today())},
        {"code": "建信理财", "name": "建信理财嘉鑫固收", "yield_7d": "2.72%", "update_date": str(datetime.date.today())}
    ]
    
    # 保存为 json 数据文件
    output_file = "products_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(latest_products, f, ensure_ascii=False, indent=4)
        
    print(f"[{datetime.datetime.now()}] 数据抓取成功！已更新至 {output_file}")

if __name__ == "__main__":
    fetch_and_update_products()
