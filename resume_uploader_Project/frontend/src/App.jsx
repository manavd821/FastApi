import { BrowserRouter } from 'react-router'
import { Fragment } from 'react'
import Navigation from './routers/navigation/navigation.router'
import NavigationLayout  from './component/navigation/navigation.comonent'

function App() {
  return (
    <Fragment>
      <BrowserRouter>
          <Navigation />
      </BrowserRouter>
    </Fragment>
  )
}

export default App
