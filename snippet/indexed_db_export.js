if (!window.indexedDB) {
    console.log(`Your browser doesn't support IndexedDB`);

}
const request = indexedDB.open('localforage', 2);

request.onsuccess = (event) => {
    console.log("Success");
    var db = event.target.result;
    const txn = db.transaction('keyvaluepairs', 'readwrite');
    const store = txn.objectStore('keyvaluepairs');
    let query = store.get('FA_ROLE');

    query.onsuccess = (event) => {
        if (!event.target.result) {
            console.log(`The contact with ${FA_ROLE} not found`);
        } else {
            var myJSON = JSON.stringify(event.target.result);
            console.log(myJSON);
        }
    };
    query.onerror = (event) => {
        console.log(event.target.errorCode);
    }

    txn.oncomplete = function () {
        db.close();
    };
};
