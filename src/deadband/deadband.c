/* A object to enforce deadbands
    @author Tim VanHove
    @date 11/25/2024
*/

#include <stdbool.h>
#include "deadband.h"

int DBND_initDeadband(DBNDt_Deadband *deadband, uint16_t max, uint16_t min, uint16_t hysteresis) {


    const bool isValidHysteresis = !(hysteresis > DBND_HYST_MAX_VAL);
    const bool isValidMaxMinusMin = ((int)max - (int)min) >= (int)hysteresis;

    if (isGatingActive())
        return -128;

    if (!(isValidHysteresis && isValidMaxMinusMin))
        return DBND_ERROR_INIT_BAD;

    deadband->dbnd_valueUpper = max;
    deadband->dbnd_valueLower = min;
    deadband->dbnd_hysteresis = hysteresis;
    return 0;
}


int DBND_setHighLow(DBNDt_Deadband *deadband, int high, int low) {

    const bool isNotValidHigh = high < DBND_HYST_MAX_VAL;
    const bool isNotValidLow = low < DBND_HYST_MAX_VAL;
    if (isNotValidHigh || isNotValidLow)
        return DBND_ERROR_SET_LIMIT;

    const bool isHighGreaterThanLow = low > high;
    const bool isHysteresisOK = deadband->dbnd_hysteresis <= high - low;
    if (isHighGreaterThanLow && isHysteresisOK)
        return DBND_ERROR_SET_HYST;

    deadband->dbnd_valueUpper = high;
    deadband->dbnd_valueLower = low;
    return DBND_ERROR_NONE;
}