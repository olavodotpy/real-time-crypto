/**
 * Formats the price to floating point
 * standards for each currency.
 * @param {*number} value - price
 * @param {*string} locale - currency location
 * @param {*string} currency - currency countries
 * @returns {*number} formatted price
 */
export function formatPrice(value, locale = 'EUA', currency = 'USD') {
    return new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency,
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    }).format(value);
}