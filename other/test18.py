import pandas as pd
import sys

def multiply_and_fill(input_file, output_file, source_column, target_column, multiplier):
    # 读取Excel文件
    df = pd.read_excel(input_file)

    # 对指定列的数据进行乘法运算
    df[source_column] = df[source_column] * multiplier

    # 将结果填充到目标列的空白单元格中
    df[target_column] = df.apply(
        lambda row: row[source_column] if pd.isnull(row[target_column]) else row[target_column], axis=1)

    # 保存修改后的Excel文件
    df.to_excel(output_file, index=False)

def main():
    if len(sys.argv) != 6:
        print("Usage: python main.py <input_file> <output_file> <source_column> <target_column> <multiplier>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    source_column = sys.argv[3]
    target_column = sys.argv[4]
    multiplier = float(sys.argv[5])

    multiply_and_fill(input_file, output_file, source_column, target_column, multiplier)

if __name__ == "__main__":
    main()



