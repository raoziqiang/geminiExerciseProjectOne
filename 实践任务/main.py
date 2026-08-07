from ast import Try
from warnings import catch_warnings

from agent import Agent
def main():
    """Main function entry point."""
    # 获取用户输入的任务
    task = input("请输入任务: ")
    # 初始化Agent实例
    agent = Agent()
    # 执行任务
    result = agent.execute(task)
    # 输出任务执行结果
    print(f"任务执行结果: {result}")
    # 返回任务执行结果
    return result
    

if __name__ == "__main__":
    main()
