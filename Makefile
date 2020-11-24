.include <name.py>

USE_FREENIT = YES
SERVICE != echo ${app_name}
REGGAE_PATH := /usr/local/share/reggae
SYSPKG := YES

.include <${REGGAE_PATH}/mk/service.mk>
