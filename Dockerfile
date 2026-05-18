FROM hrishi2861/megalogin:latest

WORKDIR /app

COPY requirements.txt .
RUN uv venv && uv pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
