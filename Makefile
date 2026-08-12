# Delegates to each project's own Makefile so the monorepo has one entry point.
# Every target below exists in all three projects and runs in each of them,
# stopping at the first failure.

PROJECTS := chatbot lemon mathparser

.DEFAULT_GOAL := help
.PHONY: help check install test lint format clean

help:  ## Show this help
	@printf 'Runs the target in every project: %s\n\n' "$(PROJECTS)"
	@printf '  \033[36m%-9s\033[0m %s\n' \
		check   "Lint and test every project" \
		install "Sync dependencies in every project" \
		test    "Run every project's tests" \
		lint    "Check formatting and lint rules everywhere" \
		format  "Apply formatting and safe lint fixes everywhere" \
		clean   "Delete caches and build artefacts everywhere"
	@printf '\nRun a single project with make -C, for example: make -C lemon test\n'

check install test lint format clean:
	@for project in $(PROJECTS); do \
		printf '\n\033[1m==> %s: %s\033[0m\n' "$$project" "$@"; \
		$(MAKE) --no-print-directory -C "$$project" $@ || exit 1; \
	done
