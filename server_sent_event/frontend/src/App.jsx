import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [data, setData] = useState([])
  const [end, setEnd] = useState('')
  useEffect(()=>{
    const eventSource = new EventSource("/api/events");
    eventSource.addEventListener("end", (event) => {
      console.log("✅ Server ended stream normally.")
      setEnd(event.data)
      eventSource.close()
    })
    eventSource.onmessage = (event) => {
      const da = JSON.parse(event.data)
      setData(prev => [da, ...prev]);
    }

    eventSource.onerror = (e) => {
      if(eventSource.readyState === eventSource.CLOSED){
          console.log("✅ Stream finished intentionally.")
      }
      else{
        console.warn("EventSource failed. Closing…", e);
      }
      eventSource.close();
    };
    return () => eventSource.close();
  },[])
  

  return (
    <>
      <div>Hare Krsna</div>
      {
        data.map(da => (<div key={da.count}>
          <h4>{da.count}. {da.msg}</h4>
        </div>))
      }
      <div>{end}</div>
    </>
  )
}

export default App
