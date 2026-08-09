PYTHON ?= python3

# docs/capabilities.json is otherwise HAND-AUTHORED here (git log: "docs:
# author capabilities.json for the stapel-catalog sweep") — stapel-social is a
# composite preset (preset.py wires stapel-chat/profiles/reviews together)
# with no _capabilities.py / _codegen.py pipeline of its own, so there is
# nothing to regenerate provides/axes/extension_points/requires from. `make
# contract` DOES now patch the two derivable things: module/version from
# pyproject, and the `surface` section (discoverability-design.md §1.2) — the
# symbols a product is meant to CALL instead of writing its own.
# stapel-social's surface_roots (docs/capabilities.meta.json) is deliberately
# EMPTY: the composite has no permission classes, functions, capability
# fields or templates of its own. The rest of the document stays hand-edited.
#
# Second: docs/llms.txt (the fifth contract artifact, badge-canon §3),
# rendered from the (now-patched) capabilities.json by stapel_tools.llms_txt.
#
# README.md is the SIXTH artifact (tracker #257): assembled by
# stapel_tools.readme from docs/readme.md (the human half — what this
# composite is, how to think about it) plus everything emitted above. Badges,
# version and doc links are generated, so a release cannot leave them behind.
# Edit docs/readme.md; never README.md.
.PHONY: contract contract-check

contract:
	$(PYTHON) -m stapel_tools.surface . --patch
	$(PYTHON) -m stapel_tools.llms_txt .
	$(PYTHON) -m stapel_tools.readme .

contract-check:
	$(PYTHON) -m stapel_tools.surface . --patch --check
	$(PYTHON) -m stapel_tools.llms_txt . --check
	$(PYTHON) -m stapel_tools.readme . --check
