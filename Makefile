run:
	lsof -i :8501 | awk 'NR!=1 {print $$2}' | xargs -r kill -9
	streamlit run main.py