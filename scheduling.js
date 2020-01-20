// How do you make a function that takes f and returns a function that calls f on a timeout?

function scheduleTask(timeout, func) {
    return function() {
        setTimeout(func, timeout)
    }
}