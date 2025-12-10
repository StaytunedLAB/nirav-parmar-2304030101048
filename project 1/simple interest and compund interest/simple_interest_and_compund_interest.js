//simple interest = P * R * T / 100
function simpleInterest(principal, rate, time) {
    return (principal * rate * time) / 100;
}           

//compound interest = P * (1 + R/100)^T - P
function compoundInterest(principal, rate, time) {
    return principal * Math.pow((1 + rate / 100), time) - principal;
}   