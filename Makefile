# !make

# Google Cloud Settings
DEFAULT_CONFIG = default
EMULATOR_CONFIG = emulator
EMULATOR_HOST = localhost:9010

GOOGLE_APPLICATION_CREDENTIALS = /Users/kazu0716/.config/gcloud/application_default_credentials.json
GOOGLE_CLOUD_PROJECT = spanner-django-demo

.PHONY: create.emulatorConfig
create.emulatorConfig:
	@gcloud config configurations create $(EMULATOR_CONFIG)
	@gcloud config set auth/disable_credentials true
	@gcloud config set project $(GOOGLE_CLOUD_PROJECT)
	@gcloud config set api_endpoint_overrides/spanner http://localhost:9020/

.PHONY: load.local
load.local:
    @export SPANNER_EMULATOR_HOST=$(EMULATOR_HOST)
    @export GOOGLE_APPLICATION_CREDENTIALS=$(GOOGLE_APPLICATION_CREDENTIALS)
    @export GOOGLE_CLOUD_PROJECT=$(GOOGLE_CLOUD_PROJECT)

.PHONY: emulator.enable
emulator.enable:
	@gcloud config configurations activate $(EMULATOR_CONFIG)

.PHONY: emulator.disable
emulator.disable:
	@gcloud config configurations activate $(DEFAULT_CONFIG)