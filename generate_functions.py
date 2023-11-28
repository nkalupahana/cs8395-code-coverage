import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from tqdm import tqdm
from time import sleep

# Generate a sample Python function with one numeric argument that manipuates that argument. Only use very basic arithmetic, like addition and subtraction. Do not use any if or for statements. Be sure to return your final result. Include just the function, and name it {branch}.
# Generate a sample Python function with one string argument that manipuates that argument. Do not use any if or for statements. Be sure to return your final result. Include just the function, and name it {branch}.
# Generate a sample Python function with one numeric argument that manipuates that argument. Include an if statement with no else ifs in that manipulation. Be sure to return your final result. Include just the function, and name it {branch}.
# Generate a sample Python function with one string argument that manipuates that argument. Include an if statement with else ifs in that manipulation. Be sure to return your final result. Include just the function, and name it {branch}.
# Generate a sample Python function with one numeric argument that manipuates that argument. Include an if statement, and another if statement nested inside of it, in that manipulation. Be sure to return your final result. Include just the function, and name it {branch}.
# Generate a sample Python function with two string arguments that manipuate those arguments. Include an if statement, and then another if statement after it that depends on the result of the first if statement, in that manipulation. The if statements should not be nested. Be sure to return your final result. Include just the function, and name it {branch}.

generation = "one/string/seq-if"
os.makedirs(f"functions/{generation}", exist_ok=True)
llm = OpenAI(max_tokens=2048)
prompt = PromptTemplate.from_template("Generate a sample Python function with one string argument that manipuates that argument. Include an if statement, and then another if statement after it that depends on the result of the first if statement, in that manipulation. The if statements should not be nested. Be sure to return your final result. Include just the function, and name it {branch}.")

sleep(1)
for i in tqdm(range(10)):
    code_prompt = prompt.format(branch=f"ex{i}")
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    with open(f"functions/{generation}/ex{i}.py", "w") as f:
        f.write(output)