import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto max-w-md rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping line-chart */}<div obj="line-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping slider */}<div obj="slider">
                  <input type="range" className="w-full" />

</div>
            </div>
          </div>
        </div>

        {/* Row 2 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-5 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping line-chart */}<div obj="line-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-5 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping bar-chart */}<div obj="bar-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 3 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-11 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping textarea */}<div obj="textarea">
                  <textarea className="w-full rounded border p-2" rows="4">
              </textarea>

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-9 col-start-2">
            <div className="flex gap-2">
{/* Object Mapping pie-chart */}<div obj="pie-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 5 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-11 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping slider */}<div obj="slider">
                  <input type="range" className="w-full" />

</div>
            </div>
          </div>
        </div>

        {/* Row 6 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-1 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping radio-button */}<div obj="radio-button">
                  <input type="radio" className="h-4 w-4" />

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-10">
            <div className="flex gap-2">
{/* Object Mapping switch */}<div obj="switch">
                  <label className="inline-flex items-center gap-2">
                <input type="checkbox" className="sr-only" />
                <span className="w-10 h-5 bg-gray-300 rounded-full"></span>
              </label>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
