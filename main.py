"""
TODO
1. testDataFile为fixtures文件夹下的测试数据文件名，例如传入的值为"testData.txt"，注意并不包含文件路径。
2. 你写的程序将把testDataFile作为参数加载此文件并读取文件内的测试数据，并对每条测试数据计算结果。
3. 将所有计费结果拼接并使用\n分割，然后保存到resultt变量中。
"""
import argparse
from fizzbuzz import process_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-data",
                        type=str,
                        required=True,
                        metavar="./resource/testData.txt",
                        help="test data path")
    args = parser.parse_args()
    test_data_file = args.test_data
    result = process_file(test_data_file)
    print(result)
