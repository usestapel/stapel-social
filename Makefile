PYTHON ?= python3

# docs/capabilities.json is HAND-AUTHORED here (git log: "docs: author
# capabilities.json for the stapel-catalog sweep") — stapel-social is a
# composite preset (preset.py wires stapel-chat/profiles/reviews together)
# with no _capabilities.py / _codegen.py pipeline of its own, so there is
# nothing to regenerate capabilities.json from. DO NOT point contract/
# contract-check at it, and do not attempt to regenerate it — the curated
# content would be lost.
#
# These targets manage ONLY docs/llms.txt (the fifth contract artifact,
# badge-canon §3), rendered from the curated capabilities.json by
# stapel_tools.llms_txt.
.PHONY: contract contract-check

contract:
	$(PYTHON) -m stapel_tools.llms_txt .

contract-check:
	$(PYTHON) -m stapel_tools.llms_txt . --check
