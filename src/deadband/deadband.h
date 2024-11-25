/* A interface for deadband enforcement
    @author Tim VanHove
    @date 11/25/2024
*/

#include <stdint.h>

#define DBND_HYST_MAX_VAL 0x0FFF

#define DBND_ERROR_INIT_BAD -3
#define DBND_ERROR_SET_HYST -2
#define DBND_ERROR_SET_LIMIT -1
#define DBND_ERROR_NONE 0

typedef struct DBND_struct {
    uint16_t dbnd_hysteresis; ///< The Value that should not be enforced
    uint16_t dbnd_valueUpper; ///< The upper value
    uint16_t dbnd_valueLower; ///< The lower value
} DBNDt_Deadband;

int DBND_initDeadband(DBNDt_Deadband *deadband, uint16_t max, uint16_t min, uint16_t hysteresis);

int DBND_setHighLow(DBNDt_Deadband *deadband, int high, int low);