from browserpilot.agents.gpt_selenium_agent import GPTSeleniumAgent



# init main
def main():

    instructions_file = "prompts/examples/instagram.yaml"
    edge_driver_path = "./edgedriver_win64/msedgedriver.exe"
    chrome_driver_path = "./chromedriver-win64/chromedriver.exe"
    compiled_instructions_file = "output/instagram.yaml"
    chrome_user_data = "C:Users/ted/AppData/Local/Google/Chrome/User Data"

    with open(instructions_file, "r") as f:
        instructions = f.read()

    agent = GPTSeleniumAgent(
        instructions = instructions,
        chromedriver_path = chrome_driver_path,
        instruction_output_file = compiled_instructions_file,
        user_data_dir = chrome_user_data
        )
    
    agent.run()


# run main
if __name__ == "__main__":
    main()