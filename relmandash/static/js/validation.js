function checkLength( o, n, min, max ) {
    if ( o.val().length > max || o.val().length < min ) {
        o.addClass( "ui-state-error" );
        updateTips( "Length of " + n + " must be between " +
        min + " and " + max + "." );
        return false;
    } else {
        return true;
    }
}
function checkRegexp( o, regexp, n ) {
    if ( !( regexp.test( o.val() ) ) ) {
        o.addClass( "ui-state-error" );
        updateTips( n );
        return false;
    } else {
        return true;
    }
}
