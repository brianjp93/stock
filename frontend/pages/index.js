import styles from '../styles/Home.module.css'
import Link from 'next/link'

export default function Home() {
  return (
    <div className={styles.container}>
      <h1>
        Welcome to Stock or something
      </h1>

      <div>
        <ul>
          <li>
            <Link href='/item/10/'>
              <a>Item 10</a>
            </Link>
          </li>
        </ul>
      </div>
    </div>
  )
}
