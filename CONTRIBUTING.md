# Contributing to EchoX

Thank you for your interest in contributing to EchoX! We welcome contributions from everyone. This document provides guidelines and instructions for contributing to the project.

## 🤝 Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read and adhere to our principles of respect and inclusivity in all interactions.

---

## 💡 How Can I Contribute?

### Reporting Bugs

Before creating a bug report, check the issue list to avoid duplicates.

**How to submit a bug report:**

1. Use a clear and descriptive title
2. Describe the exact steps to reproduce the problem
3. Provide specific examples to demonstrate the steps
4. Describe the observed behavior and what you expected
5. Include screenshots or error messages if applicable
6. Include your environment (Windows version, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

1. Use a clear and descriptive title
2. Provide a step-by-step description of the suggested enhancement
3. Provide specific examples to demonstrate the steps
4. Describe the current behavior and expected behavior
5. Explain why this enhancement would be useful

### Pull Requests

- Follow the existing code style and conventions
- Include appropriate test cases
- Update documentation as needed
- Keep commits atomic and well-organized
- Write clear commit messages

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (venv or similar)

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/EchoX.git
cd EchoX

# Add upstream remote
git remote add upstream https://github.com/akra2017linux-rgb/EchoX.git
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
pip install pytest flake8 black  # Development tools
```

### Step 4: Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

---

## 📋 Coding Standards

### Style Guide

- Follow [PEP 8](https://pep8.org/) for Python code
- Use meaningful variable and function names
- Keep functions focused and modular
- Add docstrings to classes and functions
- Maximum line length: 100 characters (where reasonable)

### Example of Well-Formatted Code

```python
def get_music_files(directory_path: str) -> list[str]:
    """
    Scan directory recursively for MP3 files.
    
    Args:
        directory_path (str): Path to the directory to scan
        
    Returns:
        list[str]: List of MP3 file paths found
        
    Raises:
        ValueError: If directory_path is invalid
    """
    if not os.path.isdir(directory_path):
        raise ValueError(f"Invalid directory: {directory_path}")
    
    music_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.mp3'):
                music_files.append(os.path.join(root, file))
    
    return music_files
```

### Formatting

Use Black for automatic code formatting:

```bash
black main.py utils/
```

### Linting

Use flake8 to check code quality:

```bash
flake8 .
```

---

## ✅ Testing

Before submitting a pull request, ensure your code works correctly:

```bash
# Run the application
python main.py

# Manually test your feature
# Run any existing tests
pytest
```

---

## 📝 Commit Messages

Write clear, descriptive commit messages:

```
feat: Add album artwork extraction feature
^--^  ^------------------------------^
|     |
|     +-> Summary in present tense (max 50 chars)
+-------> Type: feat, fix, docs, style, refactor, test, chore
```

### Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without feature or fix changes
- **test**: Adding or updating tests
- **chore**: Build process, dependencies, or tooling changes

### Examples

```
feat: Add shuffle mode toggle
fix: Resolve crash when loading corrupted MP3
docs: Update installation guide
refactor: Simplify playlist loading logic
```

---

## 🔄 Submitting Pull Requests

### Before You Start

1. Ensure your fork is up to date with upstream
2. Create a new branch for your feature
3. Make your changes
4. Test thoroughly

### Pull Request Process

1. **Update your branch**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what changed and why
   - Reference to related issues (e.g., "Closes #123")
   - Screenshots if applicable
   - Checklist of testing done

4. **PR Template Example**:
   ```
   ## Description
   Brief description of the changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Testing
   - [ ] Tested on Windows 10
   - [ ] Manual testing completed
   - [ ] No new errors introduced
   
   ## Related Issues
   Closes #123
   ```

### Code Review

- Be open to feedback and suggestions
- Respond to review comments promptly
- Make requested changes in new commits
- Re-request review after making changes

---

## 📚 Documentation

### Documentation Standards

- Keep documentation up to date with code changes
- Write in clear, simple English
- Use examples where appropriate
- Include type hints in function signatures

### Areas That Need Documentation

- README.md - Project overview and quick start
- Code comments - Complex logic and non-obvious code
- Docstrings - Functions, classes, and modules
- CHANGELOG.md - Version history (when applicable)

---

## 🚀 Release Process

Maintainers follow this process for releases:

1. Update version numbers
2. Update CHANGELOG
3. Create a release tag
4. Generate Windows installer
5. Create GitHub Release with installers

---

## 📞 Questions?

- Check existing [GitHub Issues](https://github.com/akra2017linux-rgb/EchoX/issues)
- Create a [GitHub Discussion](https://github.com/akra2017linux-rgb/EchoX/discussions) for questions
- Look at existing code and tests for examples

---

## 🙏 Thank You!

Your contributions make EchoX better for everyone. We appreciate your time and effort!

Happy coding! 🎵
