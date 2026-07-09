# Quick Start Guide

Get up and running with the API Testing Framework in 5 minutes.

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Run Your First Test

```bash
pytest tests/test_posts.py -v
```

## 3️⃣ Run All Tests

```bash
pytest -v
```

## 4️⃣ Run Smoke Tests Only

```bash
pytest -m smoke -v
```

## 5️⃣ Generate HTML Report

```bash
pytest --html=report.html --self-contained-html
```

## 6️⃣ Run Tests in Different Environment

```bash
# Windows
set TEST_ENV=qa
pytest

# Linux/Mac
export TEST_ENV=qa
pytest
```

## 7️⃣ View Test Logs

```bash
# View latest log file
type logs/api.log
# or
cat logs/api.log
```

## 📊 Test Results

- ✅ Tests pass if API returns expected status codes and responses
- ❌ Tests fail if assertions don't match expectations
- 📝 All requests are logged in `logs/api.log`

## Common Commands

```bash
# Run specific test file
pytest tests/test_posts.py

# Run specific test function
pytest tests/test_posts.py::test_create_post

# Run with coverage
pytest --cov=api --cov=utils

# Run with extra verbose output
pytest -vv

# Run tests in parallel (requires pytest-xdist)
pytest -n auto
```

## 🔧 Next Steps

1. Review the [readme.md](readme.md) for detailed documentation
2. Check existing tests in `tests/` folder
3. Add new test cases following the same patterns
4. Modify API endpoints in `config/qa.json` as needed

## ❓ Troubleshooting

**Tests not running?**
- Ensure Python is installed: `python --version`
- Ensure dependencies are installed: `pip install -r requirements.txt`
- Check internet connection (tests use live API)

**Import errors?**
- Make sure you're running pytest from the project root directory
- Verify conftest.py is in the root directory

**Tests timing out?**
- Check your internet connection
- Verify the API is accessible: `curl https://jsonplaceholder.typicode.com/posts`

Happy testing! 🚀
