# runnable sequence ki help sa bohat sa runnable ko sequence connect kar sakte hai aur jaise yeh connect karo toh first wale runnable ka output second wale runnbale ka input ban jae ga 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableLambda
from dotenv import load_dotenv
load_dotenv()
# sab sa pehle hum prompt template bannae ga 
prompt1 =PromptTemplate(
    template='write a joke about {topic}',
    input_variables={'topic'}
)
# is ka baad hum model bannae ga
model = ChatGroq(model="openai/gpt-oss-120b")
# is ka baad parser bannae ga 
parser=StrOutputParser()
prompt2=PromptTemplate(
    template='explain the following joke - {text}',
    input_variables={'text'}
)
# 5. Formatter Function: Yeh pehle parser ke string output ko {'text': '...' } dict mein badle ga
# taake prompt2 ko sahi format mein input mile.
format_for_prompt2 = RunnableLambda(lambda joke_text: {"text": joke_text})
# ab humare pass teeno runnable ban gaye hai ab hum chain bannae ga
# ma apna sequence sa apne runnable pass karne hote hai
chain = RunnableSequence(prompt1,model,parser,format_for_prompt2,prompt2,model,parser)
# sath hi hum is ka result ko rprint kare ga
print(chain.invoke({'topic':'Ai'}))