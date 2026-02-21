# Contributing to ReliefWatch

Thank you for your interest in contributing to ReliefWatch.

This project monitors humanitarian crises, which means errors and design choices can have real-world implications. Please read this guide carefully before contributing.

---

## Before You Start

**Understand the scope:** ReliefWatch focuses on early-warning signals for humanitarian needs in specific geographic regions. Features that fall outside this scope will likely not be accepted.

**Understand the constraints:** This system processes sensitive information about vulnerable populations. All contributions must consider privacy, security, and potential misuse.

---

## Types of Contributions

### Accepted

- **Bug fixes** with clear reproduction steps
- **Language model evaluation** for Arabic dialects and regional languages
- **Geographic normalization** improvements for covered regions
- **Documentation** corrections and translations
- **Test coverage** improvements
- **Performance optimizations** that don't compromise accuracy
- **Integration code** for humanitarian data standards (HDX, IATI, OCHA APIs)

### Requires Discussion First

- New language support (open an issue with validation plan)
- New geographic regions (requires evaluation data)
- Changes to classification categories
- New data source integrations
- User-facing output format changes

### Not Accepted

- Features that enable real-time targeting or tactical use
- Integrations with non-public data sources
- Changes that remove source attribution
- "AI" branding or marketing language
- Accuracy claims without supporting evaluation data

---

## Development Process

1. **Check existing issues** before starting work
2. **Open an issue** for significant changes before submitting a PR
3. **Fork the repository** and create a feature branch
4. **Write tests** for new functionality
5. **Update documentation** as needed
6. **Submit a pull request** with a clear description

---

## Code Standards

- Clear, readable code over clever optimizations
- Explicit error handling with informative messages
- Comments explaining *why*, not *what*
- No hardcoded credentials or API keys
- Type hints for Python code
- Consistent formatting (run linters before submitting)

---

## Evaluation Requirements

Changes to classification or extraction logic must include:

1. Evaluation on held-out test data
2. Performance metrics (precision, recall, F1) with confidence intervals
3. Failure case analysis
4. Comparison to previous version

Do not claim accuracy improvements without supporting data.

---

## Ethical Guidelines

When contributing, consider:

- **Privacy:** Could this change expose vulnerable individuals?
- **Misuse:** Could this feature be repurposed for surveillance or targeting?
- **Bias:** Does this change affect coverage of certain populations?
- **Transparency:** Are limitations clearly documented?

If you're unsure, ask in the issue discussion before implementing.

---

## Review Process

All pull requests require review by a maintainer. Reviews focus on:

- Correctness and test coverage
- Security implications
- Documentation completeness
- Alignment with project goals

Reviews may take time. This project is maintained by a small team.

---

## Code of Conduct

Be professional. Be respectful. Focus on the work.

Harassment, discrimination, and bad-faith engagement will result in removal from the project.

---

## Questions?

Open a GitHub issue or contact the maintainers directly.
