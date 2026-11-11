# runnable parallel hume parallel chains banne ma help karta hai aur is maa dono chains paralle excute hooga dono input same input mile aur dono ka output dick ki form milta hai 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
load_dotenv()
# hum do runnable ko parallel excute karao ga aik sath kaam aur post aik ka kaam post genrate karna 
prompt1=PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables={'topic'}
)
prompt2=PromptTemplate(
    template='Generate a linkedin post about {topic}',
    input_variables={'topic'}
)
model=ChatGroq(model='openai/gpt-oss-120b')
parser=StrOutputParser()
# ab hum aik parallel chain banne ga jis mutiple chain excute hoogi aur is ka liye hum runnable sequence 
parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke({'topic':'transformer'})
print(result)
print(result['tweet'])