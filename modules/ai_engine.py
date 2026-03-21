import google.generativeai as genai
import streamlit as st

def get_ai_advice(problem_description):
    try:
        # Puxa a chave que você configurou no settings.py ou secrets
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Usando a versão ultra rápida 2026
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt_mestre = """
        Você é o InjexFlow AI. Especialista em injeção plástica. 
        Analise o problema (rebarba, peça curta, queima) e sugira 
        ajustes em Temperatura, Pressão ou Velocidade. Seja técnico e direto.
        """
        
        response = model.generate_content([prompt_mestre, problem_description])
        return response.text
    except Exception as e:
        return f"Erro na IA: {str(e)}"
