#include "gating.h"

int g_is_gating_active = 0;

int isGatingActive(void) {
    return g_is_gating_active;
}

void setGatingStatus(int status) {
    g_is_gating_active = status;
}
