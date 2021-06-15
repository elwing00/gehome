import bidict

from .erd_oven_cook_mode import ErdOvenCookMode
from .erd_oven_state import ErdOvenState
from .oven_cook_mode import OvenCookMode

# Translate OVEN_COOK_MODE values into something easier to work with
OVEN_COOK_MODE_MAP = bidict.bidict({
    ErdOvenCookMode.BAKED_GOODS: OvenCookMode(ErdOvenState.OVEN_STATE_BAKED_GOODS, False, False, False),
    ErdOvenCookMode.BAKETIMEDSHUTOFF_DELAYSTART: OvenCookMode(ErdOvenState.BAKE, True, True, False),
    ErdOvenCookMode.BAKETIMED_TWOTEMP: OvenCookMode(ErdOvenState.BAKE_TWO_TEMP, False, True, False),
    ErdOvenCookMode.BAKETIMED_TWOTEMP_DELAYSTART: OvenCookMode(ErdOvenState.BAKE_TWO_TEMP, True, True, False),
    ErdOvenCookMode.BAKETIMED_WARM: OvenCookMode(ErdOvenState.WARM, False, True, False),
    ErdOvenCookMode.BAKETIMED_WARM_DELAYSTART: OvenCookMode(ErdOvenState.WARM, True, True, False),
    ErdOvenCookMode.BAKE_DELAYSTART: OvenCookMode(ErdOvenState.BAKE, True, False, False),
    ErdOvenCookMode.BAKE_NOOPTION: OvenCookMode(ErdOvenState.BAKE, False, False, False),
    ErdOvenCookMode.BAKE_PROBE: OvenCookMode(ErdOvenState.BAKE, False, False, True),
    ErdOvenCookMode.BAKE_PROBE_DELAYSTART: OvenCookMode(ErdOvenState.BAKE, True, False, True),
    ErdOvenCookMode.BAKE_SABBATH: OvenCookMode(ErdOvenState.BAKE, False, False, False, False, True),
    ErdOvenCookMode.BROIL_HIGH: OvenCookMode(ErdOvenState.BROIL_HIGH, False, False, False),
    ErdOvenCookMode.BROIL_LOW: OvenCookMode(ErdOvenState.BROIL_LOW, False, False, False),
    ErdOvenCookMode.CONVBAKETIMEDSHUTOFF_DELAYSTART: OvenCookMode(ErdOvenState.CONV_BAKE, True, True, False),
    ErdOvenCookMode.CONVBAKETIMED_TWOTEMP: OvenCookMode(ErdOvenState.CONV_BAKE_TWO_TEMP, False, True, False),
    ErdOvenCookMode.CONVBAKETIMED_TWOTEMP_DELAYSTART: OvenCookMode(ErdOvenState.CONV_BAKE_TWO_TEMP, True, True, False),
    ErdOvenCookMode.CONVBAKETIMED_WARM: OvenCookMode(ErdOvenState.CONV_BAKE, False, True, False, True),
    ErdOvenCookMode.CONVBAKETIMED_WARM_DELAYSTART: OvenCookMode(ErdOvenState.CONV_BAKE, True, True, False, True),
    ErdOvenCookMode.CONVBAKE_DELAYSTART: OvenCookMode(ErdOvenState.CONV_BAKE, True, False, False),
    ErdOvenCookMode.CONVBAKE_NOOPTION: OvenCookMode(ErdOvenState.CONV_BAKE, False, False, False),
    ErdOvenCookMode.CONVBAKE_PROBE: OvenCookMode(ErdOvenState.CONV_BAKE, False, False, True),
    ErdOvenCookMode.CONVBAKE_PROBE_DELAYSTART: OvenCookMode(ErdOvenState.CONV_BAKE, True, False, True),
    ErdOvenCookMode.CONVBROILCRISP_NOOPTION: OvenCookMode(ErdOvenState.CONV_BROIL_CRISP, False, False, False),
    ErdOvenCookMode.CONVBROILCRISP_PROBE: OvenCookMode(ErdOvenState.CONV_BROIL_CRISP, False, False, True),
    ErdOvenCookMode.CONVBROIL_HIGH_NOOPTION: OvenCookMode(ErdOvenState.CONV_BROIL_HIGH, False, False, False),
    ErdOvenCookMode.CONVBROIL_LOW_NOOPTION: OvenCookMode(ErdOvenState.CONV_BROIL_LOW, False, False, False),
    ErdOvenCookMode.CONVMULTIBAKETIMEDSHUTOFF_DELAYSTART: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, True, True, False),
    ErdOvenCookMode.CONVMULTIBAKETIMED_TWOTEMP: OvenCookMode(ErdOvenState.CONV_MULTI_TWO_BAKE, False, True, False),
    ErdOvenCookMode.CONVMULTIBAKETIMED_TWOTEMP_DELAYSTART: OvenCookMode(ErdOvenState.CONV_MULTI_TWO_BAKE, True, True, False),
    ErdOvenCookMode.CONVMULTIBAKETIMED_WARM: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, False, True, False, True),
    ErdOvenCookMode.CONVMULTIBAKETIMED_WARM_DELAYSTART: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, True, True, False, True),
    ErdOvenCookMode.CONVMULTIBAKE_DELAYSTART: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, True, False, False),
    ErdOvenCookMode.CONVMULTIBAKE_NOOPTION: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, False, False, False),
    ErdOvenCookMode.CONVMULTIBAKE_PROBE: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, False, False, True),
    ErdOvenCookMode.CONVMULTIBAKE_PROBE_DELAYSTART: OvenCookMode(ErdOvenState.CONV_MUTLI_BAKE, True, False, True),
    ErdOvenCookMode.CONVROASTTIMEDSHUTOFF_DELAYSTART: OvenCookMode(ErdOvenState.CONV_ROAST, True, True, False),
    ErdOvenCookMode.CONVROASTTIMED_TWOTEMP: OvenCookMode(ErdOvenState.CONV_ROAST2, False, True, False),
    ErdOvenCookMode.CONVROASTTIMED_TWOTEMP_DELAYSTART: OvenCookMode(ErdOvenState.CONV_ROAST2, True, True, False),
    ErdOvenCookMode.CONVROASTTIMED_WARM: OvenCookMode(ErdOvenState.CONV_ROAST, False, True, False, True),
    ErdOvenCookMode.CONVROASTTIMED_WARM_DELAYSTART: OvenCookMode(ErdOvenState.CONV_ROAST, True, True, False, True),
    ErdOvenCookMode.CONVROAST_DELAYSTART: OvenCookMode(ErdOvenState.CONV_ROAST, True, False, False),
    ErdOvenCookMode.CONVROAST_NOOPTION: OvenCookMode(ErdOvenState.CONV_ROAST, False, False, False),
    ErdOvenCookMode.CONVROAST_PROBE: OvenCookMode(ErdOvenState.CONV_ROAST, False, False, True),
    ErdOvenCookMode.CONVROAST_PROBE_DELAYSTART: OvenCookMode(ErdOvenState.CONV_ROAST, True, False, True),
    ErdOvenCookMode.CUSTOMSELFCLEAN: OvenCookMode(ErdOvenState.CUSTOM_CLEAN_STAGE2, False, False, False),
    ErdOvenCookMode.CUSTOMSELFCLEAN_DELAYSTART: OvenCookMode(ErdOvenState.CUSTOM_CLEAN_STAGE2, True, False, False),
    ErdOvenCookMode.DUALBROIL_HIGH_NOOPTION: OvenCookMode(ErdOvenState.OVEN_STATE_DUAL_BROIL_HIGH, False, False, False),
    ErdOvenCookMode.DUALBROIL_LOW_NOOPTION: OvenCookMode(ErdOvenState.OVEN_STATE_DUAL_BROIL_LOW, False, False, False),
    ErdOvenCookMode.FROZEN_PIZZA: OvenCookMode(ErdOvenState.OVEN_STATE_FROZEN_PIZZA, False, False, False),
    ErdOvenCookMode.FROZEN_PIZZA_MULTI: OvenCookMode(ErdOvenState.OVEN_STATE_FROZEN_PIZZA_MULTI, False, False, False),
    ErdOvenCookMode.FROZEN_SNACKS: OvenCookMode(ErdOvenState.OVEN_STATE_FROZEN_SNACKS, False, False, False),
    ErdOvenCookMode.FROZEN_SNACKS_MULTI: OvenCookMode(ErdOvenState.OVEN_STATE_FROZEN_SNACKS_MULTI, False, False, False),
    ErdOvenCookMode.NOMODE: OvenCookMode(ErdOvenState.NO_MODE, False, False, False),
    ErdOvenCookMode.PROOF_DELAYSTART: OvenCookMode(ErdOvenState.PROOF, True, False, False),
    ErdOvenCookMode.PROOF_NOOPTION: OvenCookMode(ErdOvenState.PROOF, False, False, False),
    ErdOvenCookMode.STEAMCLEAN: OvenCookMode(ErdOvenState.STEAM_CLEAN_STAGE2, False, False, False),
    ErdOvenCookMode.STEAMCLEAN_DELAYSTART: OvenCookMode(ErdOvenState.STEAM_CLEAN_STAGE2, True, False, False),
    ErdOvenCookMode.WARM_DELAYSTART: OvenCookMode(ErdOvenState.WARM, True, False, False),
    ErdOvenCookMode.WARM_NOOPTION: OvenCookMode(ErdOvenState.WARM, False, False, False),
    ErdOvenCookMode.WARM_PROBE: OvenCookMode(ErdOvenState.WARM, False, False, True),
})