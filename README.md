# Expense Tracker MCP Server

An **MCP Server** built using **FastMCP**, integrated with **Supabase (PostgreSQL)** and **SQLAlchemy ORM**, and designed to work seamlessly with **Claude Desktop** using resources and tools primitives.

---

## 🚀 Features

- Hosted on **MCP Cloud**  
- Connected to **Supabase PostgreSQL** database  
- Uses **SQLAlchemy ORM** and **Pydantic** models  
- Integrates smoothly with **Claude Desktop** (MCP client)

---

## 🧩 Dependencies

```txt
fastmcp>=2.13.0.2
psycopg2>=2.9.11
psycopg2-binary>=2.9.11
pydantic-settings>=2.11.0
sqlalchemy>=2.0.44
```

Install dependencies (recommended using `uv`):

```bash
uv sync
```

---

## 🏗️ Project Structure

```
expense-tracker-mcp/
│
├── .env                      # Environment variables (Supabase URL, DB config, etc.)
├── .gitignore
├── .python-version
├── categories.json            # Category mappings or static data
├── fastmcp.json               # FastMCP configuration file
├── main.py                    # Entry point for MCP server
├── pyproject.toml             # Project metadata and dependencies
├── uv.lock                    # uv dependency lock file
├── README.md                  # Project documentation
│
├── database/                  # Database-related modules
│   ├── __pycache__/           
│   ├── crud.py                # CRUD operations for records
│   ├── database.py            # DB connection setup
│   ├── models.py              # SQLAlchemy models
│   └── schemas.py             # Pydantic schemas
│
└── __pycache__/               # Compiled Python cache files
```

---

## ⚙️ Usage

### 1. Run MCP Inspector

```bash
uv run fastmcp dev main.py
```

### 2. Install MCP Server in Claude Desktop

```bash
uv run fastmcp install claude-desktop main.py
```

After installation, update your `claude_desktop_config.json`:

```json
"args": [
  "--directory",
  "D:\\Practice-Projects\\expense-tracker-mcp",
  "run",
  "fastmcp",
  "run",
  "main.py"
]
```

---

## 🧠 Notes

- Ensure your **Supabase connection string** is properly configured in `.env`.  
- The server communicates through **MCP Cloud** and uses **Claude Desktop** as the client.  

---

## 🪪 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Umar Ehtisham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
